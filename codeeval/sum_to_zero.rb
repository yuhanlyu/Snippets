require 'set'
File.open(ARGV[0]).each_line do |line|
    values = line.split(',').map(&:to_i).each_with_index.to_a.combination(2)
             .each_with_object(Hash.new(){|h,k| h[k] = []}){|((vi,i),(vj,j)),vs|
                vs[vi + vj] << [i, j]
             }
    puts values.each_key.select {|v| v >= 0 && values.has_key?(-v)}
               .each_with_object(Set.new()) {|value, ans|
                   values[value].product(values[-value]).map(&:flatten)
                                .map(&:uniq).select {|p| p.size == 4}
                                .map(&:sort).each {|p| ans << p}
    }.size
end
