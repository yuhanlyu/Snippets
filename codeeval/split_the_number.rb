File.open(ARGV[0]).each_line do |line|
    nums, eqn = line.chomp.split
    pos, sign = eqn.index('+'), 1
    (pos, sign = eqn.index('-'), -1) if pos.nil?
    n1, n2 = nums[0...pos].to_i, nums[pos..-1].to_i
    puts n1 + sign * n2
end
