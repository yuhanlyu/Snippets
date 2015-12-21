File.open(ARGV[0]).each_line do |line|
    n, nums = line.split(";")
    n, nums = n.to_i, nums.split.map(&:to_i)
    result = nums[0...n].inject(:+)
    (0...nums.size - n).each_with_object([result]) do |i, cur|
        cur[0] = cur[0] - nums[i] + nums[i + n]
        result = [cur[0], result].max
    end
    puts result > 0 ? result : 0
end
