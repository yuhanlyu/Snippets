File.open(ARGV[0]).each_line do |line|
    line = line.chomp
    if line.length > 55
        index = line[0...40].rindex(' ')
        line = (index ? line[0...index] : line[0...40]) + '... <Read More>'
    end
    puts line
end
