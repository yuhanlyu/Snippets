File.open(ARGV[0]).each_line do |line|
    puts line.chomp.split.map { |sym| sym[0].upcase + sym[1..-1] }.join(" ")
end
