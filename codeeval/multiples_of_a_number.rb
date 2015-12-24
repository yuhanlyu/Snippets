File.open(ARGV[0]).each_line do |line|
    x, n = line.split(',').map(&:to_i)
    multiple = n + n
    multiple += n until multiple >= x
    puts multiple
end
