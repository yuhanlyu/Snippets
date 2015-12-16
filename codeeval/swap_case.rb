File.open(ARGV[0]).each_line do |line|
    print line.swapcase
end
