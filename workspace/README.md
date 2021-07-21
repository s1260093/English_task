# Readme.md
redtaskの説明

# Requirement
・Python  
  NLTK  
  inflection  
  
# Installation
```pip install nltk```  
```pip install inflection```  

# Solutions
## 読み込み  
sample.CSVファイルを読み込む（同じディレクトリに置くこと）  
一行目がタイトルになるはずなので、line[0][0]を収納  
縦長のグラフの場合：  
 左が月、右が数値になるはずなので、line[i][0]をmonthリスト、line[i][1]をvalueリストに収納  
横長のグラフの場合：  
 上が月、下が数値になるはずなので、line[i][0]〜line[i][MAX]までをmonthリスト、line[i+1][0]〜line[i+1][MAX]までをvalueリストに収納  
  
  
## 言語処理  
NLTKを使用し、タイトルを単語ごとに分割、POSタグ判定をする  
A of B の形の場合：  
 間のof(POS:"IN")を検知、Aをheadに、Bをtailに収納  
A B の形（上記以外）の場合：   
 文中にofがないことを確かめ、Aをheadに、Bをtailに収納  
  
上記処理の後、headとtailを小文字に変換  
  
  
## タイトル作成  
headとtailを組み合わせて、５つのタイトル文を作成する  
  
  
## アウトプット  
数字の増減を確かめて、それに対応した文を出力する  
増減に対応する動詞はそれぞれ３つあり、３つ目を出力すると１番目に戻る（ループ）  



