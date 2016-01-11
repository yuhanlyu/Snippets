c, ans = [1, 5, 10, 25, 50], [1] + [0] * 100
c.each {|coin| coin.upto(100) {|i| ans[i] += ans[i - coin] } }
File.open(ARGV[0]).each_line do |line|
    puts ans[line.to_i]
end
