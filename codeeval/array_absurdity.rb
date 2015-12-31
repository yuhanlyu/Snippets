File.open(ARGV[0]).each_line do |line|
    nums = line.split(";")[1].split(",").map(&:to_i)
    puts nums.inject((0..nums.size - 2).inject(:^),:^)
end
