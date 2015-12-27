File.open(ARGV[0]).each_line.map(&:to_i).map do |remainder|
    puts [5, 3, 1].each.inject(0) { |ans, denom|
        quotient, remainder = remainder.divmod(denom)
        ans += quotient
    }
end
