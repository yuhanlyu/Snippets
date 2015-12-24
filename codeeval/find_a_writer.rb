File.open(ARGV[0]).each_line do |line|
    code, positions = line.split("|")
    puts positions.split.map(&:to_i).map{ |i| code[i - 1] }.join
end
