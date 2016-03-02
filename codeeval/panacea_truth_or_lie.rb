File.open(ARGV[0]).each_line do |line|
    virus, anti = line.split("|")
    v = virus.split(" ").map {|x| x.to_i(16)}.inject(:+)
    a = anti.split(" ").map {|x| x.to_i(2)}.inject(:+)
    puts v <= a ? "True" : "False"
end
