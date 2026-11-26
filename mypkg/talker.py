import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node 
from person_msgs.srv import Query

rclpy.init()                     #rclpyの初期化（最初に1回）
node = Node("talker")            #ノード作成（nodeという「オブジェクト」を

def cb(request, response):
    if request.name == "鈴木太郎":   #変更: 依頼（request）のnameを見る
        response.age = 41           #変更: 返事（response）のageに年齢を入れる
    else:
        response.age = 255          #変更: 知らない人なら255
    return response                 #変更: 返事を返す

def main():
    srv = node.create_service(Query, "query", cb)   #変更: サービスを作成（型、名前、関数）
    rclpy.spin(node)

