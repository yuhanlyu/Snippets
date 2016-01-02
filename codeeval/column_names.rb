File.open(ARGV[0]).each_line do |line|
    n, ans = line.to_i, []
    while n > 0
        n, remainder = (n - 1).divmod(26)
        ans.unshift(("A".ord + remainder).chr)
    end
    puts ans.join
end
