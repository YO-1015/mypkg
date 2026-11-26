import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import Int16   #通信の型（16ビットの符号付き整数）
from person_msgs.msg import Person

rclpy.init()                     #rclpyの初期化（最初に1回）
node = Node("talker")            #ノード作成（nodeという「オブジェクト」を作成）
pub = node.create_publisher(Person, "person", 10)   
n = 0                            #カウント用変数
def cb():               #タイマーで定期的に呼ばれるコールバック関数
    global n            #関数を抜けてもnがリセットされないようにしている
    msg = Person()       
    msg.name = "YO-1015"
    msg.age = n % 256
    pub.publish(msg)    #pubの持つpublishでメッセージ送信（パブリッシュ）
    n += 1


def main():
    node.create_timer(0.5, cb)  #0.5秒ごとにcbを呼ぶタイマー
    rclpy.spin(node)            #実行（無限ループ。タイマーや送受信を処理し続ける）

