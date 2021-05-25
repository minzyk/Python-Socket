from modbus_tk import modbus_rtu_over_tcp
import modbus_tk.defines as cst




client = modbus_rtu_over_tcp.RtuOverTcpMaster(host='192.168.0.45',port=502,timeout_in_sec=1)
read_input_data = client.execute(slave=1, function_code=cst.READ_HOLDING_REGISTERS, starting_address=0, quantity_of_x=10)

print(read_input_data)

#it write the values 77,88,99 (its in a list because you can write multiple values) on register 64001,64002 and read the informarion at 64100 until 64108.
#read_write_data = client.execute(slave=unit, function_code=cst.READ_WRITE_MULTIPLE_REGISTERS, starting_address=64100, quantity_of_x=9, output_value=[77,88,99], write_starting_address_FC23=64000)