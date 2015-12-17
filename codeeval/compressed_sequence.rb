File.open(ARGV[0]).each_line do |line|
    nums = line.chomp.split(' ').map(&:to_i)
    current, count = nums[0], 0
    nums.each do |num|
        if num == current
            count += 1
        else
            print sprintf("%d %d ", count, current)
            current, count = num, 1
        end
    end
    print sprintf("%d %d\n", count, current)
end
