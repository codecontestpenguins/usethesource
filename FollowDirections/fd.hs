import Control.Monad.State

type Position = (Int, Int)

data Direction = North | East | South | West
    deriving (Show, Eq, Enum)

data RoboState = RS { dir :: Direction, pos :: Position }

type Robo = State RoboState

initialState = RS { dir = North, pos = (0,0) }

turn :: String -> Robo ()
turn d = do
    d <- gets dir
    let i = fromEnum d
        d' = toEnum $ (i + 1) `mod` 4 
    modify (\s -> s { dir = d' })

move :: Int -> Robo ()
move n = do
    d <- gets dir
    p <- gets pos
    modify (\s -> s { pos = addP (vec d) p })


liftP2 f (ax, ay) (bx, by) = (f ax bx, f ay by)

addP = liftP2 (+)

vec :: Direction -> Position
vec North = (0,1)
vec South = (0,-1)
vec East = (1,0)
vec West = (-1,0)
