File.open(ARGV[0]).each_line do |line|
    nums = line.split
    puts nums.each_slice(Math.sqrt(nums.length)).to_a
             .transpose.map(&:reverse).flatten.join(" ")
end
