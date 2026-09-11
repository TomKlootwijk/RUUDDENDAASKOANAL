; Tom Klootwijk Gambit 4.0 -- reaction_nonnegative_mass
(set-option :produce-proofs true)
(set-option :timeout 15000)
(declare-const u Int)(declare-const v Int)(declare-const a Int)(declare-const b Int)
(assert (and (>= u 0) (>= v 0) (<= 0 a u) (<= 0 b v)))
(define-fun un () Int (+ (- u a) b))(define-fun vn () Int (+ (- v b) a))
(assert (not (and (>= un 0) (>= vn 0) (= (+ un vn) (+ u v)))))
(check-sat)
(get-proof)
