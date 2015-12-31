File.open(ARGV[0]).each_line do |line|
    nums, k = line.split(";")
    puts nums.split(",").each_slice(k.to_i).map {|l| 
        l.size == k.to_i ? l.reverse : l
    }.reduce(:+).join(",")
end
