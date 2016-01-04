File.open(ARGV[0]).each_line do |line|
    h, v = line[1...-2].split(") (").map {|s| s.split(",").map(&:to_f)}
    v, i, j, it = v.map {|i| i * h[-1] / v[-1]}, 0, 0, 0
    while i < h.size && j < v.size do
        case h[i] <=> v[j]
        when 0
            it, i, j = it + 1, i + 1, j + 1
        when -1
            i += 1
        else
            j += 1
        end
    end
    puts h.size + v.size - it - 1
end
