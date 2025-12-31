# XY平面座標物体の位置シミュレーション
![test](https://github.com/Little-Horese-0314/mypkg/actions/runs/20618423641/job/59215523805)

## 概要
- このパッケージは、2次元平面上の座標 (x, y) を操作する ROS 2 パッケージ である。
- 上下左右の移動、座標のリセットを行うことができる。
- 実際のロボットの移動をする際、縦と横に何メートル移動したかをわかりやすく表示させるためのものである。

## 必要なソフトウェア
- python
	- テスト済みバージョン3.5~3.10

##　テスト環境
- Ubuntu 24.04 LTS
- ros2

## コマンドの種類
- up --- y+1
- down --- y-1
- right --- x+1
- left --- x-1
- reset --- x=0, y=0

## 使用方法
- ノードの起動  
 ros2 run mypkg talker

- サービス呼び出し例  
 ros2 service call /move person_msgs/srv/Query "{command: 'up'}"

- 出力例  
 x: 1  
 y: 2  

## 著作権
このソフトウェアパッケージは3条項BSDライセンスの元再頒布および使>用が許可されます 2025 Koma Tsutsumi  
- Copyright (c) 2025 Koma Tsutsumi
