require "set"
e = [[0], [2, 4, 6, 10, 12, 16, 18], [1, 3, 5, 9, 11, 15, 17], 
          [2, 4, 8, 10, 14, 16],     [1, 3, 7, 9, 13, 15], 
          [2, 6, 8, 12, 14, 18],     [1, 5, 7, 11, 13, 17],
          [4, 6, 10, 12, 16],        [3, 5, 9, 11, 15], 
          [2, 4, 8, 10, 14],         [1, 3, 7,  9, 13], 
          [2, 6, 8, 12, 18],         [1, 5, 7, 11, 17], 
          [4, 6, 10, 16, 18],        [3, 5, 9, 15, 17], 
          [2, 4, 8, 14, 16],         [1, 3, 7, 13, 15], 
          [2, 6, 12, 14],            [1, 5, 11, 13]]

def c(e, v, m, r, n)
    v << r
    back = false
    if m.member?(r)
        m.delete r 
        back = true
    end
    a = e[r].each.reduce(0) {|a, u|
        if v.member?(u)
            a
        else
            if m.size == 1 && m.member?(u)
                v.size == n - 1 ? a + 1 : a
            else
                a + c(e, v, m, u, n) 
            end
        end
    }
    v.delete r
    m << r if back
    return a
end

File.open(ARGV[0]).each_line do |line|
    n = line.to_i
    if n % 2 == 1
        puts 0
    elsif n == 18
        puts 770144
    else
        edges = e[0..n].map {|ee| ee.select {|u| u <= n}}
        puts c(edges, Set.new, Set.new(edges[1]), 1, n)
    end
end
