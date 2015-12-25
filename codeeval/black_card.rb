File.open(ARGV[0]).each_line do |line|
    names, n = line.split(" | ")
    names, n = names.split, n.to_i - 1
    names.delete_at(n % names.length) until names.length == 1
    puts names[0]
end
