File.open(ARGV[0]).each_line do |line|
    n, m = line.split.map(&:to_i)
    if m == 1
        puts n - 1
        next
    end
    ans, m = (n - (n / 2)) + n / 6, m % 2
    ans -= (n + 3) / 6 if m == 0 
    if n % 2 == 0
        ans += (n % 3 == 0) ? -1 : 1
    elsif n % 3 == 0
        ans += (m == 1) ? -1 : 1
    else
        ans -= 1
    end
    puts ans
end
