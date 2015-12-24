File.open(ARGV[0]).each_line do |line|
    d = line.chomp.split(";").map {|i| i.split(",")[1].to_i}.sort
    puts d.each_cons(2).each_with_object([d[0]]) {|(b, a), r| r<<a-b}.join(",")
end
