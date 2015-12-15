File.open(ARGV[0]).each_line do |line|
    nums = line.chomp.split(",").map(&:to_i)
    count = 0
    candidate = nums[0]
    nums.each do |x|
        if count == 0
            candidate = x
            count = 1
        else
            count += x == candidate ? 1 : -1
        end
    end
    puts nums.count(candidate) > nums.length / 2 ? candidate : "None"
end
