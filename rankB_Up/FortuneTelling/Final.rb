# 次のような占いプログラムを作成してください。

# 「ユーザー」と「ユーザーに対応する血液型」、「血液型」と「血液型に対応する占い結果」が与えられます。

# それぞれのユーザーに対応する占い結果を表示してください。

# 入力例の1つ目は、ユーザーの血液型についてのラッキーカラーの占いです。

# 入力例の2つ目は、ユーザーの星座についてのラッキーパーソンの占いになっています。
# 「血液型」として「星座」などのさまざまな文字列を利用できるようにすることで、他の占いにも対応する必要があることに注意してください。



n = gets.to_i
name_target = {}

n.times do
    name, target = gets.chomp.split(" ")
    name_target[name] = target
end


m = gets.to_i
target_output = {}
m.times do
    target, output = gets.chomp.split(" ")
    target_output[target] = output
end

name_target.each do |name, target|
    puts name + " " + target_output[target]
end
