File.open(ARGV[0]).each_line do |line|
    a, n = line.split(" | ")
    a, n = a.split.map(&:to_i), [n.to_i, a.size - 1].min
    (1..n).each do |k|
        (0...a.size - k).each {|i| a[i], a[i+1] = a[i+1], a[i] if a[i] > a[i+1]}
    end
    puts a.join(" ")
end
