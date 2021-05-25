import TFRD_RTU_OVER_TCP as Over_tcp
from modbus_tk import modbus_rtu_over_tcp
import modbus_tk.defines as cst
import threading
import pymysql

"""
class Modbus:
    def __init__(self):
        self.connMB = modbus_rtu_over_tcp.RtuOverTcpMaster(host='192.168.0.45', port=502, timeout_in_sec=1)
        #self.connDB = Over_tcp.client()

        self.tableIndex = [
            'analog_input',
            'coil_output',
            'descret_input',
            'holding_input'
        ]

        self.idx_table = list()
        self.idx_column = list()

        # ===== 여기에서 밑의 클래스 데이터베이스부분에 값을 append해 줄거임 ===
        for i in range(len(self.tableIndex)):
            self.idx_table.append(self.conv_table_index)
        # END


    def getData(self):
        self.get_data = self.connDB.execute(slave=1, function_code=cst.READ_HOLDING_REGISTERS, starting_address=0, quantity_of_x=10)
        # self.read_db = Over_tcp.read_input_data()
        print(self.get_data)


    #def setData(self):
    #    self.set_data = self.connDB.excute()
"""


class Database:
    def __init__(self):
        self.connDB = pymysql.connect(
            host='192.168.0.117',
            port=3306,
            database='TFRD_2021_SNBD',
            user='admin',
            password='tf654321',
            charset='utf8'
        )
        """
    def readDB(self, qry):
        read_db = self.connDB.cursor()
        read_db.execute(qry)

    def writeDB(self, qry):
        write_db = self.connDB.cursor()
        write_db.execute(qry)
        """


class Main:
    def __init__(self):
        database = Database()


if __name__ == "__main__":
    Main = Database()


"""모드버스 값을 불러올거임 이걸 db랑 연결

1. 모드버스에서 가져온 값(프로토콜 설정)
2. DB에 넣어주기
3. DB에 있는 값을 PHP 웹 사이트에서 볼 수 있게 구현
class Main: 만들어서 리스트 append 시킬 값들, 
 
 """


# read data한거를 DB에 update해줘야한다






