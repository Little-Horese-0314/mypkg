# mypkg

このソフトウェアパッケージは3条項BSDライセンスの元再頒布および使用が許可されます 2025 Koma Tsutsumi

# 概要
- このパッケージは、2次元平面上の座標 (x, y) を操作する ROS 2 パッケージ である。
- 上下左右の移動、座標のリセットを行うことができる。
- 実際のロボットの移動をする際、縦と横に何メートル移動したかをわかりやすく表示させるためのものである。

# 動作環境
- ros2
- ubuntu22.04

# コマンドの種類
- up --- y+1
- down --- y-1
- right --- x+1
- left --- x-1
- reset --- x=0, y=0

# 使用方法
- ノードの起動  
 ros2 run mypkg talker

- サービス呼び出し例  
 ros2 service call /move person_msgs/srv/Query "{command: 'up'}"

- 出力例  
 x: 1  
 y: 2  

# 著作権
- Copyright (c) 2025/12/31 Koma Tsutsumi
