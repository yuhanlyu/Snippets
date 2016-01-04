tri = File.open(ARGV[0]).each_line.map {|line| line.split.map(&:to_i)}
puts (tri.size - 2).downto(0).reduce(0) { |_, i|
    (tri[i].size - 1).downto(0).reduce(0) { |_, j|
        tri[i][j] += [tri[i + 1][j], tri[i + 1][j + 1]].max
    }
}
