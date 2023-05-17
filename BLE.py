import serial
import threading
import datetime
import time
import csv
import os

def hex_to_signed_decimal(hex_str, num_bits=8):
    # 首先将16进制字符串转换为整数
    hex_num = int(hex_str, 16)

    # 检查最高有效位（符号位）是否为1
    if hex_num & (1 << (num_bits - 1)):
        # 如果符号位为1，则转换为负数
        signed_num = hex_num - (1 << num_bits)
    else:
        # 如果符号位为0，则保持原样
        signed_num = hex_num

    return signed_num

def bytes_to_hex(data):
    return " ".join(["{:02X}".format(byte) for byte in data])

def find_next_valid_start_index(buffer, start_index):
    while True:
        next_start_index = buffer.find(b'\xA5', start_index)
        if next_start_index == -1 or next_start_index == len(buffer) - 1:
            return -1
        next_byte = buffer[next_start_index + 1]
        if next_byte in (0x25, 0x26, 0x27):
            return next_start_index
        start_index = next_start_index + 1

def read_serial_data(port, baud_rate, mac, filename):
    ser = serial.Serial(port, baud_rate)
    buffer = bytearray()
    try:
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            while True:
                data = ser.read(ser.in_waiting or 1)
                if data:
                    buffer.extend(data)

                    while True:
                        start_index = find_next_valid_start_index(buffer, 0)
                        if start_index == -1:
                            break

                        next_start_index = find_next_valid_start_index(buffer, start_index + 1)
                        if next_start_index == -1:
                            break

                        # 提取子数据
                        sub_data = buffer[start_index:next_start_index]
                        hex_sub_data = bytes_to_hex(sub_data)
                        
                        if hex_sub_data[33:50] in mac and hex_sub_data[10:11] == '0':
                            rssi = hex_to_signed_decimal(hex_sub_data[6:8])
                            timestamp = time.time()
                            beacon = [timestamp,rssi,hex_sub_data[33:50]]
                            csv_writer.writerow(beacon)

                        # 移除已处理的数据
                        buffer = buffer[next_start_index:]
                        
    except KeyboardInterrupt:
        print("Terminating...")
    finally:
        ser.close()


def read_from_port(port, baud_rate,filename):
    serial_port = serial.Serial(port,baud_rate , timeout=1)
    try:
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            while True:
                if serial_port.in_waiting > 0:
                    # 读取一行数据，使用decode()方法将bytes转换为str
                    line = serial_port.readline().decode('ascii')
                    timestemps = time.time()
                    data = line.split(',')
                    if data[0] == '$GPGGA':
                        gnss_data = [timestemps,data[1],data[2],data[4],data[9]]
                        csv_writer.writerow(gnss_data)
                        csvfile.flush()
                        os.fsync(csvfile.fileno())
                        print(gnss_data)
        
    except KeyboardInterrupt:
        print("Terminating...")
    finally:
        serial_port.close()