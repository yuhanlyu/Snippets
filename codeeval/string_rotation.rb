File.open(ARGV[0]).each_line do |line|
    t, p, ans = line.chomp.split(",") + ["False"]
    if t.size == p.size
        n, i, j = t.size, 0, 0
        while i < n && j < n
            k = 1
            k += 1 while k <= n and t[(i + k) % n] == p[(j + k) % n]
            if k > n
                ans = "True"
                break
            elsif t[(i + k) % n] > p[(j + k) % n]
                i += k
            else
                j += k
            end
        end
    end
    puts ans
end
