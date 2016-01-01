File.open(ARGV[0]).each_line do |line|
    n, m = line.split(",").map(&:to_i)
    remains, cur = (0...n).to_a, 0
    puts (0...n).map {|_|
        cur = (cur + m - 1) % remains.size
        remains.delete_at(cur)
    }.join(" ")
end
