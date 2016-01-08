File.open(ARGV[0]).each_line do |line|
    n = line.split
    low, high = 0, n[0].to_i
    n.drop(1).each {|x|
        mid = low + (high - low) / 2 + (high - low) % 2
        case x
        when "Higher"
            low = mid + 1
        when "Lower"
            high = mid - 1
        else
            puts mid
        end
    }
end
