File.open(ARGV[0]).each_line do |line|
    nums = line.split(",").map(&:to_i)
    cur = ans = nums[0]
    nums.drop(1).each {|i|
        cur = [i, cur + i].max
        ans = [ans, cur].max
    }
    puts ans
end
