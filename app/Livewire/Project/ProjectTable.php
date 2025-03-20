<?php

namespace App\Livewire\Project;

use Livewire\Component;
use App\Models\Project;
use Livewire\Attributes\On; 

class ProjectTable extends Component
{

    public $projects;

    #[On('projectDelete')] 
    public function loadProjects()
    {
        $this->projects = Project::all(); // Recarga la lista de proyectos desde la base de datos
    }

    public function mount()
    {
        $this->projects = Project::all(); // Obtiene todos los proyectos
    }

    public function render()
    {
        // Inicializa la lista de proyectos si aún no se ha cargado
        if (!$this->projects) {
            $this->loadProjects();
        }

        return view('livewire.project.project-table', [
            'projects' => $this->projects,
        ]);
    }
}
