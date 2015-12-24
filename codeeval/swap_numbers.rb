File.open(ARGV[0]).each_line do |line|
    puts line.split.map {|s| s[-1] + s[1...-1] + s[0]}.join(' ')
end
