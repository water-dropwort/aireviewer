{
    inputs = {
        nixpkgs.url = "github:nixos/nixpkgs?ref=nixpkgs-unstable";
    };

    outputs =
        inputs@{
            self,
            nixpkgs,
            ...
        }:
        let
            system = "x86_64-linux";
            pkgs = nixpkgs.legacyPackages.${system};
        in {
            devShells.${system}.default = pkgs.mkShell {
                packages = [
                    pkgs.nodejs
                    pkgs.pyright
                ];
            };
            packages.${system}.default = pkgs.hello;
        };
}

