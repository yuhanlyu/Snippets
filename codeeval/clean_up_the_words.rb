File.open(ARGV[0]).each_line do |line|
    puts line.downcase.scan(/[[:alpha:]]+/).join(" ")
end
