File.open(ARGV[0]).each_line do |line|
    puts line.split(',').map{ |s| s.index('Y') - s.rindex('X') - 1}.min
end
