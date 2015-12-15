File.open(ARGV[0]).each_line do |line|
    puts line.chomp.split(" ").max_by { |x| x.length }
end
