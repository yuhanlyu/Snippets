parent = {3 => 8, 8 => 30, 10 => 20, 20 => 8, 29 => 20, 30 => nil, 52 => 30}

File.open(ARGV[0]).each_line do |line|
    n0, n1, found = *line.split.map(&:to_i), false
    loop do
        n = n1
        n = parent[n] while n && n != n0
        break if n == n0
        n0 = parent[n0]
    end
    puts n0
end
