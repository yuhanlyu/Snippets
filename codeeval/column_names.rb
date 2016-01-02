File.open(ARGV[0]).each_line do |line|
    n, result = line.to_i, []
    while n > 0
        n, remainder = (n - 1).divmod(26)
        result << ("A".ord + remainder).chr
    end
    puts result.reverse.join
end
