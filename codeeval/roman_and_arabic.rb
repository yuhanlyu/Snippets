map = {'I' => 1, 'V' => 5, 'X' => 10, 'L' => 50, 
       'C' => 100, 'D' => 500, 'M' => 1000}
File.open(ARGV[0]).each_line do |line|
    d = (0...line.size - 1).step(2).map {|i| line[i].to_i}
    r = (1...line.size - 1).step(2).map {|i| line[i]}
    puts r.each_with_index.each_cons(2).inject(0) {|sum, ((p, pi), (n, ni))|
        sum + d[pi] * map[p] * (map[n] > map[p] ? -1 : 1)
    } + d[-1] * map[r[-1]]
end
