File.open(ARGV[0]).each_line do |line|
    puts line.chomp.split(",").uniq.join(",")
end
