def c(n, k)
    return (n - k + 1..n).reduce(1, :*) / (1..k).reduce(1, :*)
end

File.open(ARGV[0]).each_line.map(&:to_i).each do |n|
    puts (0..(9 * n / 20).floor).map {|k|
        (-1) ** k * c(n, k) * c(n + (9 * n / 2).floor - 10 * k - 1, n - 1)
    }.reduce(:+)
end
