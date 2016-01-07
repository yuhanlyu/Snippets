f = File.open(ARGV[0])
track = f.readline.split.each_slice(2).map {|l| l.map(&:to_f)}
f.each_line.with_object([]) { |line, result|
        n, vmax, accel, brake = line.split
        vmax, accel, brake, vinit = vmax.to_f, accel.to_f, brake.to_f, 0
        result << [n, track.each.map {|length, angle|
            away = accel * (1 - (vinit / vmax)) * (vinit + vmax) / 7200
            vend = vmax * (1 - (angle / 180))
            bway = brake * (1 - (vend / vmax)) * (vend + vmax) / 7200
            time = 3600 * (2 * away/(vinit+vmax) + (length-away-bway)/vmax + 
                           2 * bway/(vend+vmax))
            vinit = vend
            time
        }.reduce(:+)]
    }.sort_by(&:last).map {|n, t| puts "%s %.2f" % [n, t]}
