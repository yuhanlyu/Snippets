File.open(ARGV[0]).each_line do |line|
    o, p, q, r = line.split(" ").map(&:to_i)
    case o <=> q
    when 0
        case p <=> r
        when 0 
            puts "here"
        when -1 
            puts "N"
        else
            puts "S"
        end
    when -1
        case p <=> r
        when 0 
            puts "E"
        when -1 
            puts "NE"
        else 
            puts "SE"
        end
    else
        case p <=> r
        when 0 
            puts "W"
        when -1 
            puts "NW"
        else 
            puts "SW"
        end
    end
end
