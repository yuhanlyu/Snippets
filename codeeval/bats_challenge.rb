File.open(ARGV[0]).each_line do |line|
    l, d, n, *bats = line.split.map(&:to_i)
    puts n == 0 ? (l - 12) / d + 1 :
              bats.each_cons(2).reduce(0) {|sum, (p1, p2)| sum + (p2-p1)/d-1} +
              (bats[0] - 6) / d + (l - 6 - bats[-1]) / d
end
